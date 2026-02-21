import { SceneManager } from './scene.js';
import { InteractionManager } from './interactions.js';
import { VisualizationManager } from './visualization.js';

// Initialize the 3D Scene
const sceneManager = new SceneManager('scene-container');

// Initialize Interactions
const interactionManager = new InteractionManager(sceneManager);

// Initialize Visualization (Loads data & Renders)
const vizManager = new VisualizationManager(sceneManager);
sceneManager.vizManager = vizManager; // Link for circular dependency handling (simple way)


// Load model
// Note: User can replace this with a real file path later.
// Currently using the placeholder path which triggers the fallback capsule.
// sceneManager.loadModel('path/to/human_model.glb'); 
// Or better, let's try to load a placeholder but expect fallback
sceneManager.loadModel('./assets/models/human_model.glb');  
