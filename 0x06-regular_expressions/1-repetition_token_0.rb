#!/usr/bin/env ruby
puts ARGV[0].scan(/hbt{2,5}n/).join

# {2,5}-> matches the previous token between 2 and 5 times
