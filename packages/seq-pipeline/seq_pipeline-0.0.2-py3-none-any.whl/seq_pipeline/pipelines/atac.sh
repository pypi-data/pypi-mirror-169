# --- VARIABLES ---
# > input_type = paired_fastq
BASE_PATH="{ path base_exists }"
CPU_CORES="{ integer > 0 }"
BOWTIE2_INDEX_PATH="{ path base_exists }"
BAM_WITH_DUPLICATES="{ choice keep|remove }"
BIGWIG_BIN_SIZE="{ integer > 0 }"
MACS2_CONTROL_PATH="{ optional path file_exists }"
MACS2_PVALUE="{ regex [0-9]+e-[0-9]+ }"
MACS2_GENOME_SIZE="{ regex mm|hs|cc|dm|[0-9]+ }"


# --- MODULES ---
echo "# initializing environment and loading modules $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
module reset
module load python/3.8 java/13.0
module load fastqc/0.11 bowtie2/2.4 samtools/1.12
virtualenv --no-download "$SLURM_TMPDIR/env.python.3.8"
source "$SLURM_TMPDIR/env.python.3.8/bin/activate" &&
pip install --no-index --quiet --upgrade pip &&
pip install --no-index --quiet numpy scipy matplotlib pandas deepTools==3.5.0 MACS2==2.2.7.1
chmod +x "$SLURM_TMPDIR/env.python.3.8/bin/"* 2> /dev/null


# --- FUNCTIONS ---
function reads-count {
    case "$1" in
        fastq) echo "$(zcat "$2" | wc -l) / 4" | bc ;;
        fastqx2) echo "$(zcat "$2" | wc -l) / 4 * 2" | bc ;;
        bam) samtools idxstats "$2" | awk -F '\t' '{s+=$3}END{print s}' ;;
        *) echo "error: invalid format: $1" >&2 ; return 1 ;;
    esac
}
function reads-diff {
    local INITIAL="$(reads-count "$1" "$2")"
    local FINAL="$(reads-count "$3" "$4")"
    local PERCENT="$(echo "scale=2 ; $FINAL / $INITIAL * 100" | bc)"
    echo "reads: initial=$INITIAL final=$FINAL ($PERCENT%)"
}


# --- 1 QC AND TRIMMING ---
echo "# qc and trimming: start $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
TRIM_READS_SCRIPT_PATH="$BASE_PATH.tmp.trim_reads.py"
cat << EOM | tr -d "[:space:]" | base64 -d | gzip -dc > "$TRIM_READS_SCRIPT_PATH"
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
EOM
python "$TRIM_READS_SCRIPT_PATH" -i "$BASE_PATH.r1.fastq.gz" "$BASE_PATH.r2.fastq.gz" -a "CTGTCTCTTATA" -p "$CPU_CORES"
rm "$TRIM_READS_SCRIPT_PATH"
fastqc --quiet -t "$CPU_CORES" "$BASE_PATH.r1.fastq.gz" "$BASE_PATH.r2.fastq.gz" "$BASE_PATH.trimmed.r1.fastq.gz" "$BASE_PATH.trimmed.r2.fastq.gz"
rm "$BASE_PATH.r1_fastqc.zip" "$BASE_PATH.r2_fastqc.zip" "$BASE_PATH.trimmed.r1_fastqc.zip" "$BASE_PATH.trimmed.r2_fastqc.zip"
[ -d "$BASE_PATH.qc" ] || mkdir "$BASE_PATH.qc"
mv "$BASE_PATH.r1_fastqc.html" "$BASE_PATH.qc/$(basename "$BASE_PATH").r1.qc.html"
mv "$BASE_PATH.r2_fastqc.html" "$BASE_PATH.qc/$(basename "$BASE_PATH").r2.qc.html"
mv "$BASE_PATH.trimmed.r1_fastqc.html" "$BASE_PATH.qc/$(basename "$BASE_PATH").trimmed.r1.qc.html"
mv "$BASE_PATH.trimmed.r2_fastqc.html" "$BASE_PATH.qc/$(basename "$BASE_PATH").trimmed.r2.qc.html"


# --- 2 ALIGNEMENT ---
echo "# alignment: start $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
bowtie2 -p "$CPU_CORES" --fr --no-unal --no-mixed --no-discordant -x "$BOWTIE2_INDEX_PATH" -1 "$BASE_PATH.trimmed.r1.fastq.gz" -2 "$BASE_PATH.trimmed.r2.fastq.gz" |
samtools fixmate -@ "$CPU_CORES" -m /dev/stdin "$BASE_PATH.bam"


# --- 3 SORTING ---
echo "# sorting: start $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
mv "$BASE_PATH.bam" "$BASE_PATH.unsorted.bam"
samtools sort -@ "$CPU_CORES" -o "$BASE_PATH.bam" "$BASE_PATH.unsorted.bam"
samtools index -@ "$CPU_CORES" "$BASE_PATH.bam"
echo "aligned reads: $(reads-diff fastqx2 "$BASE_PATH.trimmed.r1.fastq.gz" bam "$BASE_PATH.bam")" >&2
rm "$BASE_PATH.unsorted.bam"


# --- 4 DUPLICATES ---
echo "# duplicates: start $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
mv "$BASE_PATH.bam" "$BASE_PATH.with_duplicates.bam"
mv "$BASE_PATH.bam.bai" "$BASE_PATH.with_duplicates.bam.bai"
samtools markdup -@ "$CPU_CORES" -r -s "$BASE_PATH.with_duplicates.bam" "$BASE_PATH.bam"
samtools index -@ "$CPU_CORES" "$BASE_PATH.bam"
echo "duplicates: $(reads-diff bam "$BASE_PATH.with_duplicates.bam" bam "$BASE_PATH.bam")" >&2
[ "$BAM_WITH_DUPLICATES" = remove ] && rm "$BASE_PATH.with_duplicates.bam" "$BASE_PATH.with_duplicates.bam.bai"


# --- 5 BIGWIG ---
echo "# bigwig: start $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
bamCoverage -b "$BASE_PATH.bam" -o "$BASE_PATH.cpm.bigwig" -bs "$BIGWIG_BIN_SIZE" -e 150 --normalizeUsing BPM -p "$CPU_CORES"


# --- 6 PEAK CALLING ---
echo "# peak calling: start $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
MACS2_OUTPUT_PATH="$BASE_PATH.$MACS2_PVALUE.peaks"
[ -d "$MACS2_OUTPUT_PATH" ] || mkdir "$MACS2_OUTPUT_PATH"
if [ "$MACS2_CONTROL_PATH" = "" ]; then
    macs2 callpeak -t "$BASE_PATH.bam" -n "$(basename "$BASE_PATH")" --outdir "$MACS2_OUTPUT_PATH" -f BAMPE -p "$MACS2_PVALUE" -g "$MACS2_GENOME_SIZE" --call-summits --min-length 100 --max-gap 50
else
    macs2 callpeak -t "$BASE_PATH.bam" -n "$(basename "$BASE_PATH")" --outdir "$MACS2_OUTPUT_PATH" -f BAMPE -c "$MACS2_CONTROL_PATH" -p "$MACS2_PVALUE" -g "$MACS2_GENOME_SIZE" --call-summits --min-length 100 --max-gap 50
fi
REFORMAT_MACS2_SCRIPT_PATH="$BASE_PATH.tmp.reformat_macs2.py"
cat << EOM | tr -d "[:space:]" | base64 -d | gzip -dc > "$REFORMAT_MACS2_SCRIPT_PATH"
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
EOM
python "$REFORMAT_MACS2_SCRIPT_PATH" "$MACS2_OUTPUT_PATH"
rm "$REFORMAT_MACS2_SCRIPT_PATH"


# --- DONE ---
echo "# done $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2