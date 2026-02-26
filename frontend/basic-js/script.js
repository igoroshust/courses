const makeItFunny = (str, n) => [...str].map((c, i) => (i + 1) % n ? c : c.toUpperCase()).join('');

console.log(makeItFunny('I never look back', 3));