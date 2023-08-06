# --- VARIABLES ---
# > input_type = paired_fastq
BASE_PATH="{ path base_exists }"
CPU_CORES="{ integer > 0 }"
BOWTIE2_INDEX_PATH="{ path base_exists }"
BAM_WITH_DUPLICATES="{ choice keep|remove }"
BIGWIG_BIN_SIZE="{ integer > 0 }"


# --- MODULES ---
echo "# initializing environment and loading modules $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2
module reset
export MUGQIC_INSTALL_HOME="/cvmfs/soft.mugqic/CentOS6"
module use "$MUGQIC_INSTALL_HOME/modulefiles"
module load StdEnv/2020 gcc/9.3
module load python/3.8 java/13.0
module load fastqc/0.11 bowtie2/2.4 samtools/1.12 mugqic/homer/4.11
virtualenv --no-download "$SLURM_TMPDIR/env.python.3.8"
source "$SLURM_TMPDIR/env.python.3.8/bin/activate" &&
pip install --no-index --quiet --upgrade pip &&
pip install --no-index --quiet numpy scipy matplotlib pandas deepTools==3.5.0
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
python "$TRIM_READS_SCRIPT_PATH" -i "$BASE_PATH.r1.fastq.gz" "$BASE_PATH.r2.fastq.gz" -a "AGATCGGAAGAG" -p "$CPU_CORES"
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
bamCoverage -b "$BASE_PATH.bam" -o "$BASE_PATH.fpkm.bigwig" -bs "$BIGWIG_BIN_SIZE" -e 150 --normalizeUsing RPKM -p "$CPU_CORES"


# --- DONE ---
echo "# done $(date '+%Y/%m/%d %H:%M:%S UTC%:::z')" >&2