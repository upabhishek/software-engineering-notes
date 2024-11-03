// console.log({} + [] + {} + 1)


// arr = [1,2,[8,9,10]]

// // console.log(arr.copyWithin(1,3,5))

// const array1 = [
//     [0, 1],
//     [2, 3],
//     [4, 5],
//   ];
  
//   const result = array1.reduceRight((accumulator, currentValue) =>

//     accumulator.concat(currentValue),
//   );
  
// //   const arr = [1, 2, 3];

// console.log(arr.flatMap(x => x))



//   console.log(result);



const inventory = [
  { name: "asparagus", type: "vegetables", quantity: 5 },
  { name: "bananas", type: "fruit", quantity: 0 },
  { name: "goat", type: "meat", quantity: 23 },
  { name: "cherries", type: "fruit", quantity: 5 },
  { name: "fish", type: "meat", quantity: 22 },
];

const result = Object.groupBy(inventory, ({ type }) => type);

console.log(result)