function solution(rsp) {
    let map_rsp = {'2' : '0', '0' : '5','5' : '2'};
    return rsp.split('').map(e=>map_rsp[e]).join('');
}