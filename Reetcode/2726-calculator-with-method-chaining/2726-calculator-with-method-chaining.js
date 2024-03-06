class Calculator {
    
    /** 
     * @param {number} value
     */
    
    constructor(value) {
      this.answer = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
      this.answer = this.answer + value;
      return this;
        
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
      this.answer = this.answer - value;
      return this;  
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
      this.answer = this.answer * value;
      return this;  
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
      if (value === 0 ) {
        throw new Error("Division by zero is not allowed");
      }
      this.answer = this.answer/value;
      return this;  
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
      this.answer = this.answer**value;  
      return this;
    }
    
    /** 
     * @return {number}
     */
    getResult() {
      return this.answer;
        
    }
}