import streamlit as st
import streamlit.components.v1 as components

# User input for their name
name = st.text_input("Enter the name to wish", "Friend")

fireworks_canvas_html = f"""
<html>
<head>
<style>
body, html {{{{margin:0; padding:0; height:100vh; width:100vw; background:black; overflow:hidden;}}}}
#fw-canvas {{{{
    position:fixed; top:0; left:0; width:100%; height:100%; z-index:1;
}}}}
.overlay-text {{{{
    position:fixed; left:50%; top:15%; 
    transform:translate(-50%, -50%);
    color:#FFD700; font-size:4rem; font-weight:bold;
    text-shadow:0 0 20px #ff0080, 0 0 30px #ff0000, 0 0 35px #fff, 0 0 80px #ff0040;
    z-index:3; text-align:center; user-select:none;
    pointer-events:none;
}}}}
</style>
</head>
<body>
<canvas id="fw-canvas"></canvas>
<div class="overlay-text">Happy Diwali, {name}!</div>
<script>
const canvas = document.getElementById('fw-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function randomColor() {{{{
    return 'hsl(' + Math.floor(Math.random()*360) + ',100%,60%)';
}}}}
class Particle {{{{
    constructor(x, y, angle, speed, color) {{{{
        this.x = x; this.y = y; this.angle = angle; this.speed = speed;
        this.radius = 2 + Math.random() * 2; this.friction = 0.98; this.gravity = 0.07;
        this.color = color; this.alpha = 1;
    }}}}
    update() {{{{
        this.x += Math.cos(this.angle) * this.speed;
        this.y += Math.sin(this.angle) * this.speed;
        this.speed *= this.friction;
        this.y += this.gravity;
        this.alpha -= 0.013 + Math.random()*0.017;
    }}}}
    draw(ctx) {{{{
        ctx.save();
        ctx.globalAlpha = this.alpha;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, 2*Math.PI);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.restore();
    }}}}
}}}}
class Firework {{{{
    constructor() {{{{
        this.x = Math.random()*canvas.width*0.9 + canvas.width*0.05;
        this.y = canvas.height;
        this.targetY = 200 + Math.random()*canvas.height/2;
        this.speed = 3 + Math.random()*2;
        this.color = randomColor();
        this.particles = [];
        this.exploded = false;
    }}}}
    update() {{{{
        if (!this.exploded) {{{{
            this.y -= this.speed; this.speed *= 0.98;
            if (this.y <= this.targetY) {{{{ this.explode(); this.exploded = true; }}}}
        }}}}
        for (let p of this.particles) p.update();
        this.particles = this.particles.filter(p => p.alpha > 0);
    }}}}
    draw(ctx) {{{{
        if (!this.exploded) {{{{
            ctx.save();
            ctx.beginPath();
            ctx.arc(this.x, this.y, 3, 0, 2*Math.PI);
            ctx.fillStyle = this.color;
            ctx.shadowColor = this.color; ctx.shadowBlur = 18;
            ctx.fill(); ctx.restore();
        }}}}
        for (let p of this.particles) p.draw(ctx);
    }}}}
    explode() {{{{
        for(let i=0;i<40;i++) {{{{
            let angle = Math.PI*2*i/40;
            let speed = 2+Math.random()*3;
            this.particles.push(new Particle(this.x, this.y, angle, speed, this.color));
        }}}}
    }}}}
}}}}

let fireworks = [];
function animate() {{{{
    ctx.globalCompositeOperation = 'destination-out';
    ctx.fillStyle = 'rgba(0,0,0,0.20)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = 'lighter';
    if (Math.random() < 0.048 || fireworks.length < 4) {{{{
        fireworks.push(new Firework());
    }}}}
    for (let fw of fireworks) {{{{ fw.update(); fw.draw(ctx); }}}}
    fireworks = fireworks.filter(fw => !fw.exploded || fw.particles.length > 0);
    requestAnimationFrame(animate);
}}}}
window.addEventListener('resize',()=>{{{{ 
    canvas.width = window.innerWidth; 
    canvas.height = window.innerHeight;
}}}});
animate();
</script>
</body>
</html>
"""

components.html(fireworks_canvas_html, height=800, width=1200)