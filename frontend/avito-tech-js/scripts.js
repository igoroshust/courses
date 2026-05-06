const defineMinMaxValue = array => {
	return {
		max: Math.max.apply(null, array),
		min: Math.min.apply(null, array)
	};
};

console.log(defineMinMaxValue([1, 2, 3]));
// { max: 3, min: 1 }