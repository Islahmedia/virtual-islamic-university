# Teacher Image Optimization Script
Add-Type -AssemblyName System.Drawing

function Optimize-Image {
    param(
        [string]$InputPath,
        [string]$OutputPath,
        [int]$MaxWidth = 400,
        [int]$MaxHeight = 400,
        [int]$Quality = 85
    )
    
    try {
        $originalImage = [System.Drawing.Image]::FromFile($InputPath)
        
        $originalWidth = $originalImage.Width
        $originalHeight = $originalImage.Height
        
        $ratioX = $MaxWidth / $originalWidth
        $ratioY = $MaxHeight / $originalHeight
        $ratio = [Math]::Min($ratioX, $ratioY)
        
        $newWidth = [int]($originalWidth * $ratio)
        $newHeight = [int]($originalHeight * $ratio)
        
        $newImage = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
        $graphics = [System.Drawing.Graphics]::FromImage($newImage)
        
        $graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        
        $graphics.DrawImage($originalImage, 0, 0, $newWidth, $newHeight)
        
        $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, $Quality)
        
        $newImage.Save($OutputPath, $encoder, $encoderParams)
        
        $graphics.Dispose()
        $newImage.Dispose()
        $originalImage.Dispose()
        
        $originalSize = (Get-Item $InputPath).Length
        $newSize = (Get-Item $OutputPath).Length
        $compressionRatio = [Math]::Round((1 - ($newSize / $originalSize)) * 100, 2)
        
        Write-Host "Optimized: $(Split-Path $InputPath -Leaf)" -ForegroundColor Green
        Write-Host "  Original: $([Math]::Round($originalSize/1KB, 2)) KB -> New: $([Math]::Round($newSize/1KB, 2)) KB" -ForegroundColor Cyan
        Write-Host "  Reduced by: $compressionRatio%" -ForegroundColor Yellow
        Write-Host "  Size: ${newWidth}x${newHeight}" -ForegroundColor Magenta
        Write-Host ""
        
        return $true
    }
    catch {
        Write-Host "Error: $(Split-Path $InputPath -Leaf) - $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

$optimizedDir = "Teacher Data\Optimized"
if (!(Test-Path $optimizedDir)) {
    New-Item -ItemType Directory -Path $optimizedDir -Force | Out-Null
}

Write-Host "Teacher Image Optimization Started" -ForegroundColor Yellow
Write-Host ""

$teacherImages = Get-ChildItem "Teacher Data" -Recurse -Filter "*.jpg"
$successCount = 0

foreach ($image in $teacherImages) {
    $fileName = $image.Name
    $outputPath = Join-Path $optimizedDir $fileName
    
    Write-Host "Processing: $fileName" -ForegroundColor White
    
    if (Optimize-Image -InputPath $image.FullName -OutputPath $outputPath) {
        $successCount++
    }
}

Write-Host "Optimization Complete!" -ForegroundColor Green
Write-Host "Successfully optimized: $successCount/$($teacherImages.Count) images" -ForegroundColor Cyan
Write-Host "Find optimized images in: $optimizedDir" -ForegroundColor Yellow
