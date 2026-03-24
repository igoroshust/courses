const str = 'a bc def ghij   as  as   aaaa   ';

const upperCaseShortWords = string => {
  return string
    .trim()
    .split(/\s+/)
    .map(word => word.length <= 3 ? word.toUpperCase() : word)
    .filter(Boolean) // убираем пустые строки
    .join(' ');
}

console.log('upperCaseShortWords :>> ', upperCaseShortWords(str));