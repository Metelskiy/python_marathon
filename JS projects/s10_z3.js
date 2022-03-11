function longestLogin(loginList) {
    return loginList.reduce((a, b) => (b.length >= a.length) ? b : a);
};

console.log(longestLogin(["user1", "user2", "333", "user4", "aa"]));   //  Prokopenko
//longestLogin(["user1", "user2", "333", "user4", "aa"]);   //  user4
