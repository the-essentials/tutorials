class Node

	def initialize(item)
		@left = nil
		@cargo = item
		@right = nil
	end

	def getLeft
		return @left
	end

	def getCargo
		return @cargo
	end

	def getRight
		return @right
	end

	def setLeft(newLeft)
		@left = newLeft
	end

	def setRight(newRight)
		@right = newRight
	end

end

class BinaryTree

	def initialize
		@root = nil
	end

	def insert(item)
		if @root == nil
			@root = Node.new(item)
		else
			current = @root

			while current.getRight != nil || current.getLeft != nil
				if item < current.getCargo
					if current.getLeft == nil
						current.setLeft(Node.new(item))
						return
					else
						current = current.getLeft
					end
				else
					if current.getRight == nil
						current.setRight(Node.new(item))
						return
					else
						current = current.getRight
					end
				end
			end
		end
	end

	def search(item)
		if @root == nil
			puts "There's nothing in the tree"
		else
			current = @root
			while current != nil
				if current.getCargo == item
					puts "Found "+item.to_s
					return
				else
					puts current.getCargo
					if item < current.getCargo
						current = current.getLeft
					else
						current = current.getRight
					end
				end
			end
		end
	end



end

binaryTree = BinaryTree.new

binaryTree.insert(10)
binaryTree.insert(5)
binaryTree.insert(24)
binaryTree.insert(16)

binaryTree.search(16)
