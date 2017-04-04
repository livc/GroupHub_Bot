
go run main.go
while [ $? -eq 1 ]; do
	go run main.go
done
