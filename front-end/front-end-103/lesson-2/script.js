const products = [
    { name: "Apple", price: 50 },
    { name: "Banana", price: 30 },
    { name: "Orange", price: 70 },
];

FilteredProducts = products.filter(product => product.price > 40)
console.log(`Product with price higher than 40: `)
console.log(FilteredProducts)

TaxedProducts = products.map(product => ({
    ...product,
    price: product.price * 1.1
}));
console.log(`Product with 10% tax: `)
console.log(TaxedProducts)

products.forEach((product,  index) => {
    console.log(`${index}: ${product.name} - ${product.price}`);
});

user = {
    name: "Ansar",
    age: 14,
    purchases: ["Banana", "Orange"]
}
user.email = "ansar@example.com"
user.age = 15

console.log(Object.entries(user)[2])