module DemoSimpleSync__GAL16V8_DIP__registered (clk, m1, m2, m3);

input clk;
output m1;
output m2;
output m3;

reg [2:0] count;

initial begin
  count = 3'b0;
end

// assign input pins to logic signals
// -- no assignement

// implement equations
// -- let yosys do its stuff
always @(posedge clk) begin
  if (count > 6)
    count <= 0 ;
  else
    count <= count + 1 ;
end

// assign logic signals to output
assign m1 = count[0];
assign m2 = count[1];
assign m3 = count[2];

endmodule