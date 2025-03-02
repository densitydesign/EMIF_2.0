txt2img_data_flux = {
  "clip_skip": 1,
  "stage_2_guidance": 1,
  "negative_prompt_for_image_prior": True,
  "refiner_start": 0.899999976158142,
  "sharpness": 0,
  "loras": [
    {
      "file": "hyper_flux.1__dev__8_step_lora_f16.ckpt",
      "weight": 1
    }
  ],
  "hires_fix_width": 960,
  "diffusion_tile_width": 512,
  "decoding_tile_overlap": 128,
  "model": "flux_1_dev_q8p.ckpt",
  "guiding_frame_noise": 0.0120000001043081,
  "guidance_scale": 3.5,
  "negative_aesthetic_score": 2.5,
  "target_width": 1024,
  "hires_fix": False,
  "separate_clip_l": False,
  "open_clip_g_text": None,
  "resolution_dependent_shift": True,
  "batch_size": 1,
  "seed_mode": "Scale Alike",
  "negative_original_height": 512,
  "t5_text_encoder_decoding": True,
  "hires_fix_strength": 0.600000023841858,
  "stage_2_shift": 1,
  "decoding_tile_height": 512,
  "image_prior_steps": 5,
  "negative_prompt": "",
  "original_width": 1024,
  "clip_weight": 1,
  "target_height": 1024,
  "crop_left": 0,
  "speed_up_with_guidance_embed": True,
  "aesthetic_score": 6,
  "decoding_tile_width": 512,
  "sampler": "Euler A Trailing",
  "mask_blur": 1,
  "strength": 1,
  "separate_open_clip_g": False,
  "crop_top": 0,
  "shift": 3.1581928730011,
  "fps": 5,
  "diffusion_tile_overlap": 128,
  "hires_fix_height": 960,
  "motion_scale": 127,
  "stochastic_sampling_gamma": 0.3,
  "zero_negative_prompt": True,
  "num_frames": 14,
  "negative_original_width": 512,
  "batch_count": 1,
  "prompt": "Italian family",
  "image_guidance": 1,
  "steps": 8,
  "tiled_diffusion": False,
  "diffusion_tile_height": 512,
  "width": 1024,
  "seed": 3282081781,
  "refiner_model": None,
  "preserve_original_after_inpaint": False,
  "guidance_embed": 2,
  "original_height": 1024,
  "clip_l_text": "A hyper-futuristic, surreal composition in an infinite black void. A glowing human figure, semi-translucent, entangled in a swirling field of shimmering, fractal-like flowers. The flowers radiate iridescent colors: vibrant purples, neon blues, molten golds, fiery magentas, and disintegrate into glittering particles. These particles spiral outward in elegant arcs, guided by a rotational force, creating intricate trails of light and motion.\n\nThe figure, slightly below center, has glowing circuitry beneath their semi-transparent skin, merging organic and technological aesthetics. Parts of their body stretch into luminous streaks of light, aligning with the spiraling trails. Their serene posture and upward gaze connect them to a massive black hole above, surrounded by a radiant halo of distorted light. The black hole bends space, capturing starlight and radiating fiery reds, luminous greens, shimmering whites, and vibrant blues. Glittering particles and streams of light flow upward into the vortex.\n\nThe background is a detailed galactic tapestry with vivid nebulae and glowing star clusters, softly blurred to enhance depth. Concentric waves of distortion ripple outward, subtly warping light and space, connecting the figure, flowers, and black hole in a dynamic interplay. The infinite black background emphasizes the radiant colors and motion, with lighting that dramatizes the glowing elements and their delicate, cascading shadows.\n\nA balance of creation and destruction, motion and stillness, with precise details of glitter, light trails, rotational energy, and galactic depth. The composition is alive with ethereal beauty and cosmic transcendence",
  "upscaler_scale": 2,
    "upscaler": "4x_ultrasharp_f16.ckpt",
  "mask_blur_outset": 0,
  "controls": [],
  "start_frame_guidance": 1,
  "tiled_decoding": False,
  "height": 1024
}

