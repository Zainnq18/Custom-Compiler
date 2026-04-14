! Add two numbers
program addNumbers;

var
    a : integer;
    b : integer;
    sum : integer;

begin
    write('Enter first number: ');
    read(a);
    write('Enter second number: ');
    read(b);
    sum := a + b;
    write('Sum = ');
    write(sum)
end.