#!/usr/bin/env ruby
puts ARGV[0].scan(/^\d{10}$/).join

# \d-> matches a digit (equivalent to [0-9])
# {10}-> matches the previous token exactly 10 times
