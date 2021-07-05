#!/usr/bin/env ruby
puts ARGV[0].scan(/^h.n$/).join

# ^-> asserts position at start of a line
# $-> asserts position at the end of a line
