import ezdxf
from ezdxf.gfxattribs import GfxAttribs
from ezdxf.groupby import groupby

file = ezdxf.new()
file.saveas("/Users/macos/Desktop/the_plan.dxf")
plan = ezdxf.readfile("/Users/macos/Desktop/the_plan.dxf")
msp = plan.modelspace()

doc.saveas("/Users/macos/Desktop/pycad.dxf")
msp1 = doc.modelspace()
psp = doc.paperspace()

outer_boundary_pts1 = [(0,0),(0,25),(50,25),(50,0),(0,0)]
outer_boundary1 = msp.add_lwpolyline(outer_boundary_pts1)

inner_boundary_pts1 = [(1,1),(1,24),(49,24),(49,1),(1,1)]
inner_boundary1 = msp.add_lwpolyline(inner_boundary_pts1)
doc.save()

def create_boundary(file,x1,y1,x2,y2):
    msp = file.modelspace()
    outer_boundary_pts = [(x1,y1),(x1,y2),(x2,y2),(x2,y1),(x1,y1)]
    outer_boundary = msp.add_lwpolyline(outer_boundary_pts)

    inner_boundary_pts = [(x1+1,y1+1), (x1+1, y2-1), (x2-1,y2-1), (x2-1,y1+1), (x1+1,y1+1)]
    inner_boundary = msp.add_lwpolyline(inner_boundary_pts)
    file.save()

create_boundary(doc,10,10,35,60)

line = msp1.add_lwpolyline([(11,21),(22.5,21),(22.5,11)])
msp1.add_lwpolyline([(11,20.5),(22,20.5),(22,11)])

msp1.add_lwpolyline([(11,44),(22.5,44),(22.5,59)])
msp1.add_lwpolyline([(11,44.5),(22,44.5),(22,59)])

msp1.add_lwpolyline([(34,44),(22.5,44),(22.5,59)])
msp1.add_lwpolyline([(34,44.5),(23,44.5),(23,59)])

doc.save()


any plan
lines =  msp2.query('LINE[layer == "WIN."]')

group = groupby(entities=msp2, dxfattrib="layer")

for layer,entities in group.items():
    print(layer,"\n")
    # for entity in entities:
    #     print(entity)
    # print("\n")

def layer_and_color_key(entity):
    # return None to exclude entities from the result container
    if entity.dxf.layer == "0":  # exclude entities from default layer "0"
        return None
    else:
        return entity.dxf.layer,entity.dxf.color

group2 = msp2.groupby(key=layer_and_color_key)
for key, entities in group2.items():
    print(key)
    for entity in entities:
        print(entity)
    print("-"*40)

result = msp2.query().filter(lambda e: hasattr(e, "rgb"))
if result.color=="":
    print(result.entities)

hatch = msp2.add_hatch(color=4)
hatch.paths.add_polyline_path([(0,0),(0,10),(10,10),(10,0),(0,0)])
hatch.set_pattern_fill("ANSI31", scale=2)
plan.save()

pipe = plan.blocks.new(name="CPVC_Pipe")

pipe.add_lwpolyline([(0,0),(0,20),(5,20),(5,0),(0,0)], dxfattribs={'color': 2})# doc = ezdxf.new()

block = plan.blocks.new('CPVC-Pipe')
pipe = plan.blocks.get('CPVC-Pipe')
pipe.add_lwpolyline([(0,0),(0,10),(5,10),(5,0),(0,0)])

block1 = msp.add_blockref('CPVC-Pipe',[0,0],dxfattribs={'color':5})

msp.query('REMOVE[name=="CPVC-Pipe"]')

plan.save()

p = [
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, 1, 1),
]

# MESH requires DXF R2000 or later
doc = ezdxf.new("R2000")
msp = doc.modelspace()
mesh = msp.add_mesh()

with mesh.edit_data() as mesh_data:
    mesh_data.add_face([p[0], p[1], p[2], p[3]])
    mesh_data.add_face([p[4], p[5], p[6], p[7]])
    mesh_data.add_face([p[0], p[1], p[5], p[4]])
    mesh_data.add_face([p[1], p[2], p[6], p[5]])
    mesh_data.add_face([p[3], p[2], p[6], p[7]])
    mesh_data.add_face([p[0], p[3], p[7], p[4]])
  
    mesh_data.optimize()

doc.saveas("/Users/macos/Desktop/cube_mesh_2.dxf")
