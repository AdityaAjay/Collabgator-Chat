var roomID = ["CSE","CSE3"]
var roomPWD = ["hellohellohello","hellohellohello"]

function checkPWD(id, password){
    var i = 0;
    for (room in roomID){
        if (room == id){
            if(password = roomPWD[i]){
                return true;
            }
        }
        i+=1;
    }
    return false;
}