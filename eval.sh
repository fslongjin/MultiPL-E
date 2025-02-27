IMAGE="ghcr.io/nuprl/multipl-e-evaluation"

docker run --rm --network none \
    -v ./tutorial:/tutorial:rw  \
     $IMAGE  --dir /tutorial --output-dir /tutorial --recursive