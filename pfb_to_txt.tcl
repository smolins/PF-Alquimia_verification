lappend   auto_path $env(PARFLOW_DIR)/bin
package   require parflow
namespace import Parflow::*

pfset     FileVersion    4


set file $argv
puts "$file.pfb --> $file.txt"
set input [pfload $file.pfb]

pfsave $input -sa $file.txt
