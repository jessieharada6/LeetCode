/**
 * @param {string} answerKey
 * @param {number} k
 * @return {number}
 */
 var maxConsecutiveAnswers = function(answerKey, k) {
    let output = 0
    let left = right = 0;
    let numT = numF = 0;
    
    while (right < answerKey.length) {
        if (answerKey[right] === "T") 
            numT++;
        else
            numF++;
        
        while (numT > k && numF > k) {
            if (answerKey[left] === "T")
                numT--;
            else
                numF--;
            left++;
        } 
        
        output = Math.max(output, right - left + 1);
        // if add right++ before output, then output will be added one mroe time
        right++;
    }
    
    return output
};