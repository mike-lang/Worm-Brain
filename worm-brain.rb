require 'gosu'
require 'texplay'
require 'matrix'

class FoodEnvironment
	def initialize(window)
		@window = window
		# At least to start, lets model our food environment
		# by breaking the environment up into a grid.  We'll
		# store in a matrix the quantity of food located in
		# each section of the grid
		# At least to test the visualization with something neat
		# Let's start by initializing with random values of 
		# between zero and three units of food in each section
		@food_values = Matrix.rows( 
			(0...48).to_a.map { |row_number|
				(0...64).to_a.map { |column_number|
					rand(0..3)
				}
			})
		
		
	end

	def sniff(x, y, orientation)
		# Put logic for simulated worm nose here
		# worm will invoke this method passing its position
		# and the direction (in radians) in which the nostril
		# is pointed.  Will return a value representing the food
		# density in that direction for the specified position 
		# that the worm can map to the input neurons for that nostril
	end

	def consume_food(x, y)
		# We'll have our worm consume all the food in the section
		# of the grid in which it is located.  
		# Removes the food from the section of the environment
		# in which x, y is located, and
		# returns the quantity of food consumed
		# So worm can simulate digestion 
	end

	def print
	end

	def draw
		# draws the food densities of the environment by drawing a
		# red box over the section when there is food there.
		# The brightness corresponds to the quantity of food
		# in that section.
		@food_values.each_with_index do |amount, row, col|
			if amount != 0
				color = Gosu::Color.argb(0x44440000 * amount)
				@window.draw_quad(
					col * 10, row * 10, color,
					col * 10 + 10, row * 10, color,
					col * 10 + 10, row * 10 + 10, color,
					col * 10, row * 10 + 10, color)
			end
		end
	end
end

class MyWindow < Gosu::Window
	def initialize
		super(640, 480, false)
		self.caption = 'Hello Worm Brain World!'		
		@environment = FoodEnvironment.new(self)
	end

	def update
		# run worm brain logic here for however many internal ticks
		# and update the worm's state and environment
		# and trigger actions of the worm based on the brain's 
		# output
	end

	def draw
		@environment.draw
	end
end

window = MyWindow.new
window.show

