package main
import "fmt"


func isPrime(number int) bool {
  for i := 2; i < number / 2; i++{
    if number % i == 0{
      return false
    }
  }
  
  return true
}

func main() {
  
  var number int
  
  fmt.Printf("enter number: ")
  fmt.Scan(&number)
  
  if result := isPrime(number); result{
    fmt.Printf("\nis prime")
  } else{
    fmt.Printf("\nno prime")
  }
  
}
