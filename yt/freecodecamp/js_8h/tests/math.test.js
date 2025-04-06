// math.test.js
const soma = require('../math');

test('soma 2 + 3 deve ser 5', () => {
  expect(soma(2, 3)).toBe(5);
});
