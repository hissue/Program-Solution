function solution(num_list) {
    let even_sum = 0;
    let odd_sum = 0;
    num_list.map((num, index) => {
        !(index % 2 == 0) ? even_sum += num : odd_sum += num;
    })
    return even_sum > odd_sum ? even_sum : odd_sum;
}