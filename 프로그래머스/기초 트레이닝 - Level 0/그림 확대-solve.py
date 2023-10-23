def solution(picture, k):
    answer = []
    for pixels in picture:
        new_pixels = [] 
        for pixel in pixels:
            new_pixels.append(pixel * k)
                
        for _ in range(k):
            answer.append(''.join(new_pixels))
    
    return answer