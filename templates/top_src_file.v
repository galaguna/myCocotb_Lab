`timescale 1ns/1ns

module top_module
   (
    input wire clk, rst, x,
    output reg  y
   );
   //Constants:

   //Signal declaration

   //Body

   // Dump waves
   initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, top_module);
   end

endmodule
