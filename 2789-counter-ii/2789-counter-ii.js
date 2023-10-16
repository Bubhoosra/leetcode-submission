/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    
        let c = init;
        // let p =init;
        function increment(){
            return ++c
        }
        function decrement (){
            return --c

        }
        function reset(){
            c=init
            return init
        
        }
        return {increment,decrement,reset};
}
    


/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */