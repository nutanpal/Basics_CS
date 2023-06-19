 let cart = [
  { name: 'Apple', price: 4, quantity: 2 },
  { name: 'Orange', price: 3, quantity: 3 }
];

function cartTotal(cartArray) {
  let total = 0;
  cartArray.forEach(function (item) {
    total += item.price * item.quantity;
  });
  console.log(total);
}
cartTotal(cart);


