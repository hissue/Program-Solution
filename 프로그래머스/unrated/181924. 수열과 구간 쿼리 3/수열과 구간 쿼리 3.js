function solution(arr, queries) {
    // for (let i=0; i<queries.length; i++){
    //     let [s,e] = queries[i];
    //     let temp = arr[s];
    //     arr[s] = arr[e];
    //     arr[e] = temp; 
    // }
    // return arr;
    queries.map(([s,e]) => {
        [arr[s], arr[e]] = [arr[e], arr[s]];
    })
    return arr;
}