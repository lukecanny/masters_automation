-- Title Section Start
-- VHDL testbench RISCV_RB_TB
-- Generated by HDLGen, Github https://github.com/fearghal1/HDLGen-ChatGPT, on 06-November-2023 at 18:48

-- Component Name : RISCV_RB
-- Title          : 32 x 32-bit Register Bank, with chip enable. Single synchronous write port, dual combinational read ports

-- Author(s)      : Fearghal Morgan
-- Organisation   : University of Galway
-- Email          : fearghal.morgan@universityofgalway.ie
-- Date           : 06/11/2023

-- Description    : refer to component hdl model for function description and signal dictionary
-- Title Section End
-- library declarations
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- Testbench entity declaration. No inputs or outputs
entity RISCV_RB_TB is end entity RISCV_RB_TB;

architecture behave of RISCV_RB_TB is

-- unit under test (UUT) component declaration. Identical to component entity, with 'entity' replaced with 'component'
component RISCV_RB is 
Port(
	RWr : in std_logic;
	rd : in std_logic_vector(4 downto 0);
	rs1 : in std_logic_vector(4 downto 0);
	rs2 : in std_logic_vector(4 downto 0);
	rs1D : out std_logic_vector(31 downto 0);
	rs2D : out std_logic_vector(31 downto 0);
	WBDat : in std_logic_vector(31 downto 0);
	ce : in std_logic;
	clk : in std_logic;
	rst : in std_logic 
	);
end component;

-- testbench signal declarations
signal testNo: integer; -- aids locating test in simulation waveform
signal endOfSim : boolean := false; -- assert at end of simulation to highlight simuation done. Stops clk signal generation.

-- Typically use the same signal names as in the VHDL entity, with keyword signal added, and without in/out mode keyword

signal clk: std_logic := '1';
signal rst: std_logic;        

signal RWr : std_logic;
signal rd : std_logic_vector(4 downto 0);
signal rs1 : std_logic_vector(4 downto 0);
signal rs2 : std_logic_vector(4 downto 0);
signal rs1D : std_logic_vector(31 downto 0);
signal rs2D : std_logic_vector(31 downto 0);
signal WBDat : std_logic_vector(31 downto 0);
signal ce : std_logic;

constant period: time := 20 ns; -- Default simulation time. Use as simulation delay constant, or clk period if sequential model ((50MHz clk here)
 
begin

-- Generate clk signal, when endOfSim = FALSE / 0
clkStim: clk <= not clk after period/2 when endOfSim = false else '0';

-- instantiate unit under test (UUT)
UUT: RISCV_RB-- map component internal sigs => testbench signals
port map
	(
	RWr => RWr, 
	rd => rd, 
	rs1 => rs1, 
	rs2 => rs2, 
	rs1D => rs1D, 
	rs2D => rs2D, 
	WBDat => WBDat, 
	ce => ce, 
	clk => clk, 
	rst => rst
	);

-- Signal stimulus process
stim_p: process -- process sensitivity list is empty, so process automatically executes at start of simulation. Suspend process at the wait; statement
begin
	report "%N Simulation start, time = "& time'image(now);

	-- Apply default INPUT signal values. Do not assign output signals (generated by the UUT) in this stim_p process
	-- Each stimulus signal change occurs 0.2*period after the active low-to-high clk edge
	-- if signal type is
	-- std_logic, use '0'
	-- std_logic_vector use (others => '0')
	-- integer use 0
	RWr <= '0';
	rd <= (others => '0');
	rs1 <= (others => '0');
	rs2 <= (others => '0');
	WBDat <= (others => '0');
	ce <= '0';
	report "Assert and toggle rst";
	testNo <= 0;
	rst    <= '1';
	wait for period*1.2; -- assert rst for 1.2*period, deasserting rst 0.2*period after active clk edge
	rst   <= '0';
	wait for period; -- wait 1 clock period
	
	-- START Add testbench stimulus here
	-- === If copying a stim_p process generated by ChatGPT, delete the following lines from the beginning of the pasted code
	-- === Delete the -- === notes
	-- === stim_p: process
	-- === begin


	-- ==== If copying a stim_p process generated by ChatGPT, delete the following lines from the pasted code
	-- === wait;
	-- === end process stim_p;

	-- END Add testbench stimulus here
	-- Print picosecond (ps) = 1000*ns (nanosecond) time to simulation transcript
	-- Use to find time when simulation ends (endOfSim is TRUE)
	-- Re-run the simulation for this time
	-- Select timing diagram and use View>Zoom Fit
	report "%N Simulation end, time = "& time'image(now);
	endOfSim <= TRUE; -- assert flag to stop clk signal generation

	wait; -- wait forever
end process; 
end behave;