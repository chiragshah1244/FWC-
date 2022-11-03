module seq_dec(
	input reset,
	input X,
	output reg fsm_clk,
	output reg Z
);

//declaring variables
reg	[26:0] 	delay = 0;
reg	[2:0] 	state_current = 0;
wire 		clk;
wire		q2;
wire		q1;
wire		q0;

qlal4s3b_cell_macro u_qlal4s3b_cell_macro (
	.Sys_Clk0 (clk),
);

always@(posedge clk or posedge reset)
begin
	if(reset)
		delay = 27'b0;

	else
	begin
		delay = delay + 1;
		if(delay > 20000000)
		begin
			delay = 27'b0;
			fsm_clk = !fsm_clk;
		end
	end
end

always@(posedge fsm_clk or posedge reset)
begin
	if(reset)
	begin
		state_current <= 4'b0;
		Z <= 1'b0;
	end

	else
	begin
		state_current[2] <= (!q1&X)|(q0&X);
		state_current[1] <= (q1&!q0)|(!q2&!q1&q0&!X);
		state_current[0] <= (q2)|(!q1&!q0)|(!q1&X)|(!q0&X)|(q1&q0&!X);
		Z <= (q2&!q0&!X)|(q2&q0&X);
	end
end

assign {q2,q1,q0} = state_current;

endmodule
