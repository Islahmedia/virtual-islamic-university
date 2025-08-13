# Teacher Image Optimization Script
# This script optimizes teacher images while maintaining face clarity

# Function to optimize images using System.Drawing
Add-Type -AssemblyName System.Drawing

function Optimize-TeacherImage {
    param(
        [string]$InputPath,
        [string]$OutputPath,
        [int]$MaxWidth = 400,
        [int]$MaxHeight = 400,
        [int]$Quality = 85
    )
    
    try {
        # Load the original image
        $originalImage = [System.Drawing.Image]::FromFile($InputPath)
        
        # Calculate new dimensions while maintaining aspect ratio
        $originalWidth = $originalImage.Width
        $originalHeight = $originalImage.Height
        
        $ratioX = $MaxWidth / $originalWidth
        $ratioY = $MaxHeight / $originalHeight
        $ratio = [Math]::Min($ratioX, $ratioY)
        
        $newWidth = [int]($originalWidth * $ratio)
        $newHeight = [int]($originalHeight * $ratio)
        
        # Create new bitmap with optimized size
        $newImage = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
        $graphics = [System.Drawing.Graphics]::FromImage($newImage)
        
        # Set high-quality rendering for better face clarity
        $graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        
        # Draw the resized image
        $graphics.DrawImage($originalImage, 0, 0, $newWidth, $newHeight)
        
        # Save with JPEG compression
        $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, $Quality)
        
        $newImage.Save($OutputPath, $encoder, $encoderParams)
        
        # Clean up
        $graphics.Dispose()
        $newImage.Dispose()
        $originalImage.Dispose()
        
        # Get file sizes for comparison
        $originalSize = (Get-Item $InputPath).Length
        $newSize = (Get-Item $OutputPath).Length
        $compressionRatio = [Math]::Round((1 - ($newSize / $originalSize)) * 100, 2)
        
        Write-Host "✓ Optimized: $(Split-Path $InputPath -Leaf)" -ForegroundColor Green
        Write-Host "  Original: $([Math]::Round($originalSize/1KB, 2)) KB -> Optimized: $([Math]::Round($newSize/1KB, 2)) KB" -ForegroundColor Cyan
        Write-Host "  Compression: $compressionRatio% reduction" -ForegroundColor Yellow
        Write-Host "  New dimensions: ${newWidth}x${newHeight}" -ForegroundColor Magenta
        Write-Host ""
        
        return $true
    }
    catch {
        Write-Host "✗ Error processing $(Split-Path $InputPath -Leaf): $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Create optimized images directory
$optimizedDir = "Teacher Data\Optimized"
if (!(Test-Path $optimizedDir)) {
    New-Item -ItemType Directory -Path $optimizedDir -Force | Out-Null
    Write-Host "Created directory: $optimizedDir" -ForegroundColor Green
}

Write-Host "=== Teacher Image Optimization Started ===" -ForegroundColor Yellow
Write-Host "Optimizing images for web use while maintaining face clarity..." -ForegroundColor Cyan
Write-Host ""

# Process all teacher images
$teacherImages = @()

# Find all JPG images in Teacher Data folders
Get-ChildItem "Teacher Data" -Recurse -Filter "*.jpg" | ForEach-Object {
    $teacherImages += $_.FullName
}

$successCount = 0
$totalCount = $teacherImages.Count

foreach ($imagePath in $teacherImages) {
    $fileName = Split-Path $imagePath -Leaf
    $outputPath = Join-Path $optimizedDir $fileName
    
    Write-Host "Processing: $fileName" -ForegroundColor White
    
    if (Optimize-TeacherImage -InputPath $imagePath -OutputPath $outputPath) {
        $successCount++
    }
}

Write-Host "=== Optimization Complete ===" -ForegroundColor Yellow
Write-Host "Successfully optimized: $successCount/$totalCount images" -ForegroundColor Green
Write-Host "Optimized images saved in: $optimizedDir" -ForegroundColor Cyan
Write-Host ""
Write-Host "Images are optimized for web use with:" -ForegroundColor White
Write-Host "• Maximum dimensions: 400x400 pixels" -ForegroundColor Gray
Write-Host "• High-quality bicubic interpolation for face clarity" -ForegroundColor Gray
Write-Host "• 85% JPEG quality for good compression" -ForegroundColor Gray
Write-Host "• Maintained aspect ratios" -ForegroundColor Gray
