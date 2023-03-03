FILE=timing_results.csv
touch $FILE
echo "num,linear(0),binary(1),fibonacci,notes(2)" > $FILE

for num in 1 4 22 37 22906 53757 112591 361940 475713 893766 996637 996639 996652 -996652; do
    result_string="$num"
    real_times=()
    for algo in 0 1 2; do
        time_output=$( { time ./search $algo $num >/dev/null; } 2>&1 )
        real_time=$(echo "$time_output" 2>&1 | awk '/real/ {print $2}')
        real_times+=("$real_time")
        result_string="$result_string,$real_time"
    done
    fastest_algos=()
    min_time=$(echo "${real_times[@]}" | tr ' ' '\n' | sort -n | head -n 1)
    for i in "${!real_times[@]}"; do
        if [[ "${real_times[$i]}" == "$min_time" ]]; then
            fastest_algos+=("$i")
        fi
    done
    notes=$(echo "${fastest_algos[@]}" | tr ' ' ',')
    result_string="$result_string,$notes"
    echo $result_string >> $FILE
done