module DemoSimpleTri__GAL16V8_DIP__registered (i2, i3, i4, i5, m1, m2);

input i2;
input i3;
input i4;
input i5;
output m1;
output m2;

wire [1:0] dataIn;
wire [1:0] dataOut;
wire we, ds;

// assign input pins to logic signals
assign dataIn[0] = i2;
assign dataIn[1] = i3;
assign we = ~i4;
assign ds = ~i5;

// implement equations
assign dataOut = (we & ds) ? dataIn : 2'bZZ;

// assign logic signals to output
assign m1 = dataOut[0];
assign m2 = dataOut[1];

endmodule