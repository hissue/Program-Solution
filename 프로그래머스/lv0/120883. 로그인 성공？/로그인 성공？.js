function solution(id_pw, db) {
    let [my_id, my_pw] = id_pw;
    let answer = "fail";
    for (let i=0; i< db.length; i++){
        if (db[i][0] == my_id ){
            if (db[i][1] == my_pw) answer = "login";
            else answer = "wrong pw";
        }   
    }
    return answer;
}