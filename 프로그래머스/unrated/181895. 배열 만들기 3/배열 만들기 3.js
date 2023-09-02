function solution(arr, intervals) {
    // let [x,y] = intervals;
    // let answer = [];
    // for (let i=x[0]; i<=x[1]; i++){
    //     answer.push(arr[i]);
    // }
    // for (let i=y[0]; i<=y[1]; i++){
    //     answer.push(arr[i]);
    // }
    // return answer;
    let [[a,b],[c,d]] = intervals;
    return [...arr.slice(a,b+1), ...arr.slice(c,d+1)];
}