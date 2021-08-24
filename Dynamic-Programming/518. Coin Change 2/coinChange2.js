var change = function(amount, coins) {
    let arr = Array(amount + 1).fill(0);
    arr[0] = 1;
    
    for (const coin of coins) {
        for (let i = 1; i < arr.length; i++) {
            if (i - coin >= 0) {    
                // arr[i - coin] choose the coin
                // arr[i] not choose the coin, stay as current amount
                arr[i] = arr[i - coin] + arr[i];
            } 
        }
    }
    
    // console.log(arr);
    return arr[arr.length - 1];
};