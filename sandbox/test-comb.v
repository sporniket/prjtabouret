module DemoSimpleComb__GAL16V8_DIP__registered (i2, i3, m1, m2, m3, m4, m5, m6);

// setup directionnality of the pins
// of course, declaring i* as output won’t work
input i2;
input i3;
output m1;
output m2;
output m3;
output m4;
output m5;
output m6;

wire a,b,u,v,w,x,y,z ; // logic signal to write equations/behaviour meaningfullys

// assign input pins to logic signals
assign a = i2;
assign b = i3;

// implement equations
assign u = ~a ;
assign v = a | b ;
assign w = a & b ;
assign x = ~(a & b) ;
assign y = ~(a | b) ;
assign z = (a ^ b) ;

// assign logic signals to output
assign m1 = z ;
assign m2 = y ;
assign m3 = x ;
assign m4 = w ;
assign m5 = v ;
assign m6 = u ;

endmodule