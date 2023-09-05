function solution(my_string, s, e) {
    let temp_str = my_string.split("");
    return (temp_str.slice(0,s).join("")+temp_str.slice(s,e+1).reverse().join("")+temp_str.slice(e+1).join(""));
}