let data = [
	{
		1: 11,
		2: 12,
		3: 13,
	},
	{
		1: 21,
		2: 22,
		3: 23,
	},
	{
		1: 24,
		2: 25,
		3: 26,
	},
];

console.time('ваш');
data.flatMap(Object.values).reduce((s,n)=>s+n,0);
console.timeEnd('ваш');     // ~12ms

console.time('мой');  
data.reduce((s,obj)=>s+Object.values(obj).reduce((a,b)=>a+b,0),0);
console.timeEnd('мой');     // ~8ms