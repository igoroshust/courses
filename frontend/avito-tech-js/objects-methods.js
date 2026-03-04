const user = { name: "Анна", age: 25, city: "Москва"};

// Object.assign(target, ...sources) - копирует свойства из одного или нескольких объектов в целевой объект
const defaults = { theme: "light", lang: "ru"};
const settings = { lang: "en"};
const result = Object.assign({}, defaults, settings);

// Object.freeze(obj)- замораживает объект: нельзя добавить/удалить свойства или изменить существующие
const config = { port: 3000, host: "localhost" };
Object.freeze(config);
config.port = 8000;

// Object.seal(obj) - запрещает добавление/удаление свойств, но позволяет изменить существующие
const person = { name: "Иван" };
Object.seal(person);
person.name = "Пётр"; // сработает
person.age = 30 // не сработает

// Object.create(proto[, propertiesObject]) - создаёт новый объект с указанным прототипом
const animal = { eats: true };
const dog = Object.create(animal);

// Object.getOwnPropertyNames(obj) - возвращает все собственные ключи объекта (включая неперечисляемые)
const obj = { a: 1 };
Object.defineProperty(obj, 'b', { value: 2, enumerable: false });

console.log('Object.keys(user) :>> ', Object.keys(user));
console.log('Object.values(user) :>> ', Object.values(user));
console.log('Object.entries(user) :>> ', Object.entries(user));
console.log('Object.getOwnPropertyNames(obj) :>> ', Object.getOwnPropertyNames(obj));
console.log('Object.assign:>> ', result);
console.log('Object.freeze:>> ', config.port);
console.log('Object.seal :>> ', person);
console.log('Object.create :>> ', dog.eats);