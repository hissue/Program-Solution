function sum(data) {
    return data.reduce((result,e)=> result + e);
}
function solution(arr1, arr2) {
    if (arr1.length === arr2.length){
        let sum_arr1 = sum(arr1);
        let sum_arr2 = sum(arr2);
        if (sum_arr1 === sum_arr2) return 0;
        else if (sum_arr1 > sum_arr2) return 1;
        else return -1;
    }
    else if (arr1.length > arr2.length) return 1;
    else return -1;
}