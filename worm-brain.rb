require 'gosu'
require 'texplay'
require 'matrix'

class FoodEnvironment
	def initialize(window)
		@window = window
		@food_values = Matrix.rows( 
			(0...48).to_a.map { |row_number|
				(0...64).to_a.map { |column_number|
					rand(0..3)
				}
			})
		
		
	end
	def print
		p [0...48].map { |number| number}
		p @food_values.count
		p @food_values
	end
	def draw
		@food_values.each_with_index do |amount, row, col|
			color = Gosu::Color.argb(0x44440000 * amount)
			@window.draw_quad(
				col * 10, row * 10, color,
				col * 10 + 10, row * 10, color,
				col * 10 + 10, row * 10 + 10, color,
				col * 10, row * 10 + 10, color)
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

