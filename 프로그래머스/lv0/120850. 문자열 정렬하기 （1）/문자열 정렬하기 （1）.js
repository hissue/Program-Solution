function solution(my_string) {
    return [...my_string].filter((e)=>e=='0' || +e).map((v)=>Number(v)).sort((a,b)=>a-b);
    return  [...my_string].filter((x)=>x==='0' || +x).map((v)=>Number(v)).sort((a,b)=>a-b);
}