#!/usr/bin/env ruby
puts ARGV[0].scan(/[A-Z]/).join

# A-Z-> matches a single character in the range between
#   A (index 65 in ascii table) and Z (index 90 in ascii table) (case sensitive)
