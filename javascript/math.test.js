const { add } = require('./math');

describe('add function', () => {
  it('should return the sum of two numbers', () => {
    const result = add(2, 3);
    expect(result).toBe(5); // O teste espera que a soma de 2 e 3 seja 5
  });

  it('should return a negative number when summing a positive and a larger negative number', () => {
    const result = add(5, -10);
    expect(result).toBe(-5); // O teste espera que a soma de 5 e -10 seja -5
  });

  it('should return 0 when both numbers are 0', () => {
    const result = add(0, 0);
    expect(result).toBe(0); // O teste espera que a soma de 0 e 0 seja 0
  });
});
