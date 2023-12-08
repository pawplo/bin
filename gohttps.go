package main

import (
    "fmt"; "log"; "net/http"
)

func main() {
//    fmt.Println("Port 8080")
    fmt.Println("Port 443")
    http.Handle("/", http.FileServer(http.Dir(".")))
//    err := http.ListenAndServe(":8080", nil)
    err := http.ListenAndServeTLS(":443", "/Users/air/CA/air.lan.crt", "/Users/air/CA/air.lan.key", nil)
    if err != nil {
        log.Fatal("ListenAndServe: ", err)
    }
}
