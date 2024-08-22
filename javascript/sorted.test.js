const { getSortedEvenNumbers } = require('./sorted');

it('should return sorted even numbers from an array', () => {
    const input = [5, 3, 8, 6, 7, 2];
    const output = getSortedEvenNumbers(input);
    expect(output).toEqual([2, 6, 8]);
});
    