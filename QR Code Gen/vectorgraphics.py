import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_image = qrcode.make("Hello GNV!", image_factory=factory)
svg_image.save("mysvg.svg")
