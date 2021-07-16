%полином вида [an, an-1, 
a = load('polynom.txt');
da = deriative(a);
x0 = input('Введите координаты точки. Х=');
y0 = input('Y = ');
p1 = conv(a, da);
p2 = y0.*da;
p = 2*p1 - [zeros(1, length(p1)-length(p2)), 2* p2]+ [zeros(1, length(p1)-2), 2, -2*(x0)];
r = roots(p);
r_real = r(~imag(r));
k = distanse(a, r_real, x0, y0);
i = find(k==min(k));
Xmin = r_real(i);
Ymin = polyval(a, Xmin);
xplot = -5:.01:5;
yplot = polyval(a, xplot);

plot(xplot, yplot, x0, y0, 'r.',  Xmin, Ymin, 'ok');


